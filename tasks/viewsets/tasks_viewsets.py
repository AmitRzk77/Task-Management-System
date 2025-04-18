from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from datetime import date

from ..models import Task
from ..serializers.tasks_serializers import TaskSerializer
from ..utilities.permissions import IsAdminOrAssignedUser  # Custom permission for admin/assigned users

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer 
    permission_classes = [permissions.IsAuthenticated, IsAdminOrAssignedUser]  # Ensure admin/assigned permissions

    def get_queryset(self):
        
        user = self.request.user
        queryset = Task.objects.all()
        
        if user.role != 'admin':
            queryset = queryset.filter(assigned_to=user)

        # Add status and due_date filters
        status = self.request.query_params.get('status')
        due_date = self.request.query_params.get('due_date')

        if status:
            queryset = queryset.filter(status=status)
        if due_date:
            queryset = queryset.filter(due_date=due_date)

        return queryset

    def perform_create(self, serializer):
        
        if self.request.user.role != 'admin':
            raise PermissionDenied("Only admins can assign tasks.")
        serializer.save()

    @action(detail=True, methods=['patch'], url_path='status')
    def update_status(self, request, pk=None):
        
        task = self.get_object()

        if request.user != task.assigned_to and request.user.role != 'admin':
            raise PermissionDenied("You are not allowed to update this task.")

        status_value = request.data.get('status')
        
        
        if status_value not in ['pending', 'completed']:
            return Response({"error": "Invalid status value. Choose 'pending' or 'completed'."},
                            status=status.HTTP_400_BAD_REQUEST)

        
        if status_value == 'completed' and task.due_date < date.today() and request.user.role != 'admin':
            return Response({"error": "You can't complete an overdue task unless you're an admin."},
                            status=status.HTTP_400_BAD_REQUEST)

      
        task.save()

        return Response({"message": f"Task marked as {status_value}."}, status=status.HTTP_200_OK)

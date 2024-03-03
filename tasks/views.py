from rest_framework import viewsets, permissions, status
from tasks.models import *
from tasks.serializers import TasksSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class TaskViewSet(viewsets.ModelViewSet):  # View_Basada_conjuntos
    queryset = Tasks.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TasksSerializer

# operacione extra para el view set (op personalizada)
# test use --> http://127.0.0.1:8000/api/tasks/2/review/
    @action(detail=True, methods=['post'])
    def review(self, request, pk=None):
        task = self.get_object()
        task.review = not task.review
        task.save()
        return Response({
            'status': 'task marked as review' if task.review else 'task unreview'}, status=status.HTTP_200_OK)


"""
Apuntes - 
@action: Este decorador indica que se está agregando una acción personalizada al conjunto de vistas. detail=True significa que esta acción se aplicará a un objeto específico en lugar de a la colección completa.
methods=['post']: Define que esta acción personalizada solo se puede invocar mediante solicitudes POST.
def review(self, request, pk=None): La función review realiza la acción personalizada. Obtiene el objeto task específico utilizando self.get_object(), invierte el valor de task.review y guarda los cambios. Luego, devuelve una respuesta JSON indicando el estado actual del objeto task.review.
- Bibliografia

"""

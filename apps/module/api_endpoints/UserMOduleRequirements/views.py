from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.module.models import UserModuleCompletionRequirements
from apps.module.api_endpoints.UserMOduleRequirements.serializers import UserModuleCompletionRequirementsSerializer


class UserModuleRequirementsView(RetrieveAPIView):
    queryset = UserModuleCompletionRequirements.objects.all().select_related('module')
    serializer_class = UserModuleCompletionRequirementsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        return self.queryset.filter(user=self.request.user, module_id=pk).first()


class UserModuleRequirementsUpdateView(UpdateAPIView):
    queryset = UserModuleCompletionRequirements.objects.all().select_related('module')
    serializer_class = UserModuleCompletionRequirementsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        return self.queryset.filter(user=self.request.user, module_id=pk)


__all__ = ['UserModuleRequirementsView', 'UserModuleRequirementsUpdateView']

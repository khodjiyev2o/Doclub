from rest_framework.generics import RetrieveAPIView
from apps.module.models import Module
from apps.module.api_endpoints.ModuleDetail.serializers import ModuleSerializer


class ModuleDetailView(RetrieveAPIView):
    queryset = Module.objects.prefetch_related('drugs', 'timecodes', 'pharmacist_company', 'speaker', 'module_files')
    serializer_class = ModuleSerializer


__all__ = ['ModuleDetailView']

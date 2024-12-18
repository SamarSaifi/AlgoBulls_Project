from todo_app.models.task import Task

class TaskFilterMixin:
    def get_queryset(self):
        queryset = Task.objects.all()
        return self._apply_filters(queryset)
    
    def _apply_filters(self, queryset):
        status = self.request.query_params.get('status')
        tag = self.request.query_params.get('tag')
        
        if status:
            queryset = queryset.filter(status=status)
        if tag:
            queryset = queryset.filter(tags__contains=[tag])
            
        return queryset
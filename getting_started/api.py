from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from getting_started.models import Record
from tastypie.authentication import Authentication,BasicAuthentication
from tastypie.authorization import Authorization,DjangoAuthorization
from django.contrib.auth.models import User
from tastypie import fields

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name']
        filtering = {
            'username': ALL,
        }

class EntryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True)
    
    """
    def alter_list_data_to_serialize(self, request, data):
        if data['objects']:
            data = data['objects']
        return data
    """
    
    class Meta:
        queryset = Record.objects.all()
        resource_name = 'entry'
        authentication = Authentication()
        authorization = Authorization()
        filtering = {
            'user': ALL_WITH_RELATIONS,
        }

from tastypie.resources import ModelResource
from talk.models import Talk
from tastypie.api import Api

class TalkResource(ModelResource): 
    class Meta:
        queryset = Talk.objects.all()
        resource_name = 'talk'

v1_api = Api(api_name='v1') #
v2_api = Api(api_name='v2')

#
# v1_api.register() method: Registers an instance of a Resource subclass with the API.
v1_api.register(TalkResource())
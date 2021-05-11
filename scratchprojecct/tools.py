from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



HEADER_PARAM = openapi.Parameter('Authorization', openapi.IN_HEADER, description="Example: Bearer <jwt access token>",
                                 type=openapi.TYPE_STRING)

                        
QUERY_CLASS_ID = openapi.Parameter('class', openapi.IN_QUERY, description='Class id', type=openapi.TYPE_STRING)
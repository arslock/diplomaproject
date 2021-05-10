from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



HEADER_PARAM = openapi.Parameter('Authorization', openapi.IN_HEADER, description="Example: Bearer <jwt access token>",
                                 type=openapi.TYPE_STRING)

                        

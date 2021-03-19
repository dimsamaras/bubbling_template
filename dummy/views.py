from bubbling_firebase_authentication.firebase_anonymous_permissions import IsAuthenticatedAnonymous
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticatedAnonymous])
def dummy_list(request):
    return Response({'details': 'Welcome to the dummy API'})


@api_view(['GET'])
@permission_classes([IsAuthenticatedAnonymous])
def dummy_get(request, pk):
    return Response({'details': f'You are looking for {pk} in the dummy API'})

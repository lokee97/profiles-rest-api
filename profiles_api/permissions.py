from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    #allow user to edit their own profile
    def has_object_permission(self,request,view,obj):  #HAS_OBJECT_PERMISSION IS IN-BUILT FUNCTION
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
        
class UpdateOwnStatus(permissions.BasePermission):
    #allow user to update their own status
    def has_object_permission(self,request,view,obj):
        #Check the user is trying to update their own status
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
 
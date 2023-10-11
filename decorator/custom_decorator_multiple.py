def role_required(role):
    def _role_required(func):
        @wraps
        def __role_required(*args, **kwargs):
            if not current_user.is_role(role):
                flash("You need to be authorised first to access")
                # redirect to home page
                return redirect(url_for("main.home"))
            # create() is called 
            return func(*args, **kwargs)
        return __role_required
    return _role_required

@gid.route("/create" , methods = ["GET" , "POST"])
@login_required
@role_required(Role.EMPLOYEE)
def create():
    pass

#  check if the user is logged in
#  check if the logged in user is a authorised user
#  then create the user 

                
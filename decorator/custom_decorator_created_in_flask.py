def login_required(func):
    def _login_required(*args , **kwargs):
        if current_user.is_anonymous():
            flash("You need to be logged into the page")
            return redirect(url_for("auth.login"))
        return func(*args , **kwargs)
    return _login_required
    



@auth.route("/logout")
# to logout , the func needs to check first, the user is logged in
# before logout is executed
@login_required
def logout():
    pass
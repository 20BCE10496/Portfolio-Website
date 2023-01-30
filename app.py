from flask import Flask,render_template, request
import uuid
import os
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/form/<string:design>")
def form():
    return render_template("form.html")

@app.route("/upload", methods = ["GET","POST"])
def upload():
    if request.method == "POST":
        lastname = request.form.get("lastname")
        name = request.form.get("firstname")
        school = request.form.get("school")
        college = request.form.get("college")
        phone = request.form.get("phone")
        skill1 = request.form.get("skill1")
        email = request.form.get("email")
        skill2 = request.form.get("skill2")
        skill3 = request.form.get("skill3")
        skill4 = request.form.get("skill4")
        about = request.form.get("about")
        gethub =request.form.get("github")
        linkedin=request.form.get("linkedin")
        key=uuid.uuid1()

        print(name )
        print(lastname )
        print(school)
        print(college )
        print(phone )
        print(email )
        print(skill1 )
        print(skill2 )
        print(skill3 )
        print(skill4 )
        print(about)
        
        #image upload
        img=request.files["dp"]
        img.save(f"static/images/{img.filename}")
        img_new_name=f"{key} {img.filename}"
        os.rename(f"static/images/{img.filename}",f"static/images/{img_new_name}" )
    return render_template("Design1.html",dname = name,dlname = lastname,dg= gethub, dl=linkedin, dsch = school, dcol = college,dph = phone, img= img_new_name, demail = email,ds1 = skill1,ds2 = skill2,ds3 =skill3,ds4 = skill4,dabout = about)

if __name__=="__main__":       
 app.run(debug= True)

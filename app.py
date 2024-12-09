from flask import Flask, render_template, request, jsonify
from user_utils import authenticate_user, get_username_by_name, read_user_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = authenticate_user(username, password)

        if user:
            return jsonify(status="success", name=user["Name"], bus=user["BusName"])

        return jsonify(status="error")

    return render_template("login.html")


@app.route("/profile")
def profile():
    name = request.args.get("name")
    return render_template("profile.html", name=name)


@app.route("/load")
def load():
    name = request.args.get("name")
    bus = request.args.get("bus")
    return render_template("load.html", name=name, bus=bus)


@app.route("/api/getUserProfile")
def get_user_profile():
    name = request.args.get("name")

   
    users = read_user_data() 
    print(users) 
    user = None
    for user_data in users:  
        if user_data["Name"] == name:
            user = user_data
            break

    if user:
        user_profile = {
            "Name": user.get("Name", "Not Provided"),
            "BusName": user.get("BusName", "Not Provided"),
            "Course": user.get("Course", "Not Provided"),
            "Section": user.get("Section", "Not Provided"),
            "Email": user.get("Email", "Not Provided"),
            "Route": user.get("Route", "Not Provided"),
            "PickupPoint": user.get("PickupPoint", "Not Provided"),
            "Contact": user.get("Contact", "Not Provided"),
            "EmergencyContact": user.get("EmergencyContact", "Not Provided"),
            "BloodGroup": user.get("BloodGroup", "Not Provided"),
        }
        return jsonify(user_profile)
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route("/tracking")
def tracking():
    return render_template("tracking.html")



if __name__ == "__main__":
    app.run(debug=True)

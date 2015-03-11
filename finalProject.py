from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

#import module for ORM
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, University, Room


#create connection to database
engine = create_engine("sqlite:///gotroom.db")
Base.metadata.bind=engine
DBSession = sessionmaker(bind=engine)
session=DBSession()


#create an instance of Flask class with the name
#of the runnung application as the argument
app = Flask(__name__)


@app.route("/")
@app.route("/university/")
def showUniversities():
	#get all universities from university table
	universities = session.query(University).all()
	return render_template("universities.html", universities=universities)


#add a new university
@app.route("/university/new/", methods=["GET", "POST"])
def newUniversity():
	if request.method == "POST":
		newUniversity = University(name=request.form["newUni"], city=request.form["newCity"])
		session.add(newUniversity)
		session.commit()
		return redirect(url_for("showUniversities"))
	else:
		return render_template("newuni.html")


@app.route("/university/<int:university_id>/edit/", methods=["GET", "POST"])
def editUniversity(university_id):
	#editedUni = session.query(University).filter_by(university_id=university.id)

	#if method == "POST"
	return render_template("edituni.html", university=editedUni)


@app.route("/university/<int:university_id>/delete/")
def deleteUniversity(university_id):
	return render_template("deleteuni.html", university=deletedUni)


#show rooms for a university
@app.route("/university/<int:university_id>/")
@app.route("/university/<int:university_id>/rooms/")
def showRooms(university_id):
	return render_template("rooms.html", rooms=rooms, university=university)


#create a new room for a particular university
@app.route("/university/<int:university_id>/rooms/new/")
def newRoom(university_id):
	return render_template("newroom.html", university=university)


#edit a room
@app.route("/university/<int:university_id>/<int:room_id>/edit/")
def editRoom(university_id, room_id):
	return render_template("editroom.html", university_id=university_id, room_id=room_id, room=roomToEdit)


#delete a room 
@app.route("/university/<int:university_id>/<int:room_id>/delete/")
def deleteRoom(university_id, room_id):
	return render_template("deleteroom.html",  room=roomToDelete)







if __name__ == '__main__':
	app.debug = True
	app.run("0.0.0.0", port=5000)
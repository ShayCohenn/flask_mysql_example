from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cars"
)

@app.route('/cars', methods=['GET'])
def get_cars():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cars2")
    cars_data = cursor.fetchall()
    cursor.close()
    return jsonify(cars_data)

@app.route('/cars/update/<int:id>', methods=['PATCH'])
def edit_car(id):
    data = request.get_json()
    cursor = db.cursor()
    set_clause = ", ".join([f"{key} = '{data[key]}'" for key in data])
    sql = f"UPDATE cars2 SET {set_clause} WHERE car_id = {id}"
    cursor.execute(sql)
    db.commit()
    cursor.close()
    return jsonify({"message": f"Car with ID {id} updated successfully!"})

@app.route('/cars/add', methods=['POST'])
def add_car():
    data = request.get_json()
    make = data['make']
    model = data['model']
    year = data['year']
    color = data['color']

    cursor = db.cursor()
    sql = "INSERT INTO cars2 (make, model, year, color) VALUES (%s, %s, %s, %s)"
    val = (make, model, year, color)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    return jsonify({"message": "Car added successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

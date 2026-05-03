from app.db import student_collection
from bson import ObjectId

class StudentService:
    @staticmethod
    def get_all_students():
        return list(student_collection.find())

    @staticmethod
    def get_student_by_id(student_id: str):
        return student_collection.find_one({"_id": ObjectId(student_id)})

    @staticmethod
    def create_student(data: dict):
        result = student_collection.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    def update_student(student_id: str, data: dict):
        student_collection.update_one(
            {"_id": ObjectId(student_id)},
            {"$set": data}
        )

    @staticmethod
    def delete_student(student_id: str):
        student_collection.delete_one({"_id": ObjectId(student_id)})
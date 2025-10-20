from flask import jsonify, request

DB = {}  # bookID -> book dict

def create_book():
    data = request.get_json() or {}
    book_id = data.get("bookID")
    if not book_id:
        return ("bad request", 400)
    if book_id in DB:
        return jsonify({"status": "error", "message": "exists"}), 403
    DB[book_id] = {
        "bookID": book_id,
        "bookTitle": data.get("bookTitle", ""),
        "bookAuthor": data.get("bookAuthor", ""),
        "bookDescription": data.get("bookDescription", ""),
    }
    return jsonify({"status": "ok", "message": "created"}), 200

def list_books():
    return jsonify(list(DB.values())), 200

def get_book(book_id):  # was (bookID)
    book = DB.get(book_id)
    if not book:
        return ("", 404)
    return jsonify(book), 200

def update_book(book_id):  # was (bookID)
    if book_id not in DB:
        return ("", 404)
    updates = request.get_json() or {}
    for key in ["bookTitle", "bookAuthor", "bookDescription"]:
        if key in updates:
            DB[book_id][key] = updates[key]
    return jsonify(DB[book_id]), 200

def delete_book(book_id):  # was (bookID)
    if book_id not in DB:
        return ("", 404)
    DB.pop(book_id)
    return jsonify({"status": "ok", "message": "deleted"}), 200

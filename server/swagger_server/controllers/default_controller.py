from flask import jsonify, request

DB = {}  # bookID -> book dict

def create_book():  # POST /v1/book
    b = request.get_json()
    if not b or 'bookID' not in b:
        return ("bad request", 400)
    if b['bookID'] in DB:
        return jsonify({"status":"error","message":"exists"}), 403
    DB[b['bookID']] = {
        "bookID": b["bookID"],
        "bookTitle": b.get("bookTitle",""),
        "bookAuthor": b.get("bookAuthor",""),
        "bookDescription": b.get("bookDescription",""),
    }
    return jsonify({"status":"ok","message":"created"}), 200

def list_books():  # GET /v1/book
    return jsonify(list(DB.values())), 200

def get_book(bookID):  # GET /v1/book/{bookID}
    b = DB.get(bookID)
    if not b:
        return ("", 404)
    return jsonify(b), 200

def update_book(bookID):  # PUT /v1/book/{bookID}
    if bookID not in DB:
        return ("", 404)
    updates = request.get_json() or {}
    for k in ["bookTitle","bookAuthor","bookDescription"]:
        if k in updates:
            DB[bookID][k] = updates[k]
    return jsonify(DB[bookID]), 200

def delete_book(bookID):  # DELETE /v1/book/{bookID}
    if bookID not in DB:
        return ("", 404)
    DB.pop(bookID)
    return jsonify({"status":"ok","message":"deleted"}), 200

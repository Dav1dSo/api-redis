import logging
from flask import Blueprint, request, jsonify
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.redis.repository.redis_repository import RedisRepository
from src.models.mysql.repository.products_repository import ProductsRepository
from src.data.product_finder import ProductFinder
from src.data.product_create import ProductCreator


products_routes_bp = Blueprint("products_router", __name__, url_prefix="/products")

redis_repo = RedisRepository()
product_repo = ProductsRepository()

@products_routes_bp.route("/create", methods=["POST"])
def create_product():
    try:        
        product_creator = ProductCreator(redis_repo, product_repo)
        http_request = HttpRequest(body=request.json)
        http_response: HttpResponse = product_creator.create(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@products_routes_bp.route("/find-product/<int:product_id>", methods=["GET"])
def find_product(product_id):
    try:
        product_finder = ProductFinder(redis_repo, product_repo)
        http_request = HttpRequest(params={"product_id": product_id})
        http_response: HttpResponse = product_finder.find_by_name(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as err:
        logging.error(f"ERROR: {type(err)} - {err}")
        return jsonify({"error": str(err)}), 404

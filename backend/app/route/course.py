from flask import Blueprint
from flask_restful import Api
from resource.course import CourseAPI, CourseListAPI,NewsAPI, NewsListAPI, ExamAPI, ExamListAPI


course_blueprint = Blueprint("course_api", __name__)
course_blueprint_api = Api(course_blueprint)
news_blueprint = Blueprint("news_api", __name__)
news_blueprint_api = Api(news_blueprint)
exam_blueprint = Blueprint("exam_api", __name__)
exam_blueprint_api = Api(exam_blueprint)

course_blueprint_api.add_resource(
    CourseAPI, "/courses/<string:course_id>"
)
course_blueprint_api.add_resource(
    CourseListAPI, "/courses"
)

news_blueprint_api.add_resource(
    NewsListAPI, "/news"
)

news_blueprint_api.add_resource(
    NewsAPI, "/news/<string:news_id>"
)

exam_blueprint_api.add_resource(
    ExamListAPI, "/exam"
)

exam_blueprint_api.add_resource(
    ExamAPI, "/exam/<string:exam_id>"
)


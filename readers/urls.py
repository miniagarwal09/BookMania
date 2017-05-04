from django.conf.urls import url
import views
from django.contrib.auth import views as auth_views
app_name = "readers"
urlpatterns = [url(r'^homepage$', views.homepage,name="homepage"),
               url(r'^signupform$',views.signupform,name="signupform"),
               url(r'^signup_reader$',views.signup,{'type_user': 'reader'},name="signup_reader"),
               url(r'^signup_publisher$',views.signup,{"type_user":"publisher"},name="signup_publisher"),
               url(r'^logout$',views.logoutview,name='logout'),
               url(r'^login/$',auth_views.login,{'template_name': "registration/login.html"},name='login'),
               url(r'^genre_books/(?P<genre_id>[0-9]+)/$',views.books_in_genre,name="books_in_genre"),
               url(r'^book_detail/(?P<book_id>[0-9]+)/$',views.book_detail,name="book_detail"),
               url(r'^book_detail/(?P<book_id>[0-9]+)/add_review$',views.add_review,name="add_review"),
               url(r'^home$', views.home, name="home"),
               url(r'^text_review/(?P<book_id>[0-9]+)$', views.TextReviewView.as_view(), name="text_review"),
               url(r'add_book',views.add_book,name="add_book"),
               url(r'^publisher_home$',views.publisher_home,name="publisher_home")
]
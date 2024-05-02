from django.urls import path,include
from watchlist_app.views import ReviewList,ReviewCrate,\
            UserReview,WatchListAV,WatchListGV

urlpatterns = [
    path('list',WatchListAV.as_view(),name="movie-list"),
    path('list2/', WatchListGV.as_view(), name='watch-list'),
    path('<int:pk>/review-create/',ReviewCrate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/',UserReview.as_view(), name='user-review-detail')
]
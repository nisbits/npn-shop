from django.urls import path
from . import views

urlpatterns = [
   
  #  path("",views.cat_list,name="cat_list"),
   
    path("cat_list/",views.cat_list,name="cat_list"),
    path("",views.index,name="shop"),
    path("add_cat/",views.add_cat,name="add_cat"),
    path("deactivate_cat_list/<int:pk>/",views.deactivate_cat_list,name="deactivate_cat_list"),
    path("add_cat_item/<int:pk>/",views.add_cat_item,name="add_cat_item"),
     path("view_cat_wise_list/<int:pk>/",views.view_cat_wise_list,name="view_cat_wise_list"),
      path("deactivate_cat_wise_item/<int:pk>",views.deactivate_cat_wise_item,name="deactivate_cat_wise_item"),
     path('about/',views.about,name="about"),
          path('contactus/',views.contactus,name="contactus"),
          path('single_item_view/<int:pk>/',views.single_item_view,name="single_item_view"),
           path('pass_change/',views.pass_change,name="pass_change"),
            path('profile_change/',views.profile_change,name="profile_change"),
            path('pass_reset/',views.pass_forget,name="pass_reset"),
             path('add_to_cart/<int:pk>/',views.add_to_cart,name="add_to_cart"),
              path('cart/',views.cart,name="cart"),
                 path('checkout_cart/',views.checkout_cart,name="checkout_cart"),
                 path('place_order/',views.place_order,name="place_order"),
                  path('my_orders/',views.myorders,name="my_orders"),
                  path('checkout_single_item/<int:pk>/',views.checkout_single_item,name="checkout_single_item"),
                  path('single_place_order/<int:pk>/',views.single_place_order,name="single_place_order"),
                
     ]
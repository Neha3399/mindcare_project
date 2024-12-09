from django.urls import path

from new_app import views, Admin_view, counsellor_view, Patient_view
from new_app.Admin_view import accept_view


class Counsellor_view:
    pass


urlpatterns = [

    #views
    path("demo",views.demo,name="demo"),
    path("",views.land,name="land"),
    path("dash",views.dash,name="dash"),
    path("Log",views.Log,name="Log"),
    path("counsiler",views.CounsilerR,name="counsiler"),
    path("patient",views.PatientR,name="patient"),
    path("login_view",views.login_view,name="login_view"),


    #admin
    path("admin_base", Admin_view.admin_base, name="admin_base"),
    path("counsiler_view",Admin_view.table_view,name="counsiler_view"),
    path("delete/<int:id>",Admin_view.remove,name="delete"),
    path("update/<int:id>",Admin_view.update,name="update"),
    path("patient_view",Admin_view.table2_view,name="patient_view"),
    path("delete2/<int:id>",Admin_view.remove2,name="delete2"),
    path("update2/<int:id>",Admin_view.update2,name="update2"),
    path("request_accept",Admin_view.request_accept,name="request_accept"),
    path("accept/<int:id>",Admin_view.accept,name="accept"),
    path("reject/<int:id>",Admin_view.reject,name="reject"),
    path("accept_view",Admin_view.accept_view,name="accept_view"),
    path("feedback_view",Admin_view.feedback_view,name="feedback_view"),
    path("replay_feedback/<int:id>",Admin_view.replay_feedback,name="replay_feedback"),
    path("logou", Admin_view.logou, name="logou"),
    path("feedback_view_c", Admin_view.feedback_view_c, name="feedback_view_c"),
    path("replay_feedback_c/<int:id>", Admin_view.replay_feedback_c, name="replay_feedback_c"),


#counsellor

    path("counsiler_base", counsellor_view.counsiler_base, name="counsiler_base"),
    path("view_request", counsellor_view.req_donor, name="view_request"),
    path("proceed/<int:id>", counsellor_view.Donate, name="proceed"),
    path("profile_counsiler", counsellor_view.profile_counsiler, name="profile_counsiler"),
    path("profile_update/<int:id>", counsellor_view.profile_update, name="profile_update"),
    path("logou", counsellor_view.logou, name="logou"),
    path("feedbk_c",counsellor_view.feedbk_c,name="feedbk_c"),
    path("replay_c",counsellor_view.replay_c,name="replay_c"),


    #patient

    path("patient_base", Patient_view.patient_base, name="patient_base"),
    path("request", Patient_view.req, name="request"),
    path("request_view", Patient_view.req_table, name="request_view"),
    path("rmv_req/<int:id>", Patient_view.rmv_req, name="rmv_req"),
    path("feedbk", Patient_view.feedbk, name="feedbk"),
    path("replay",Patient_view.replay,name="replay"),
    path("profile_patient", Patient_view.profile_patient, name="profile_patient"),
    path("patient_update/<int:id>", Patient_view.patient_update, name="patient_update"),
    path("logou", Patient_view.logou, name="logou"),

]
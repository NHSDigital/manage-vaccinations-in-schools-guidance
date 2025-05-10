from process_images import process_booking_reminders, process_class_list_year_groups, process_clinic_invitations, process_consent_matching, process_get_consent, process_get_gillick_competent_consent, process_pre_screening, process_session_no_consent, process_sessions_add_dates, process_school_move_review

def create_images(first_session, clinic):
    IMAGES = [
        {
            "image_name": "consent-link.png",
            "path": "consent-forms",
            "screen_size": {
                "width": 1200,
                "height":1080
            },
            "further_processing": process_consent_matching
        },
        {
            "image_name": "consent-response-paper.png",
            "path": f"sessions/session-{first_session}/consent",
            "screen_size": {
                "width": 1100,
                "height": 1080
            },
            "further_processing": process_get_consent
        },
        {
            "image_name": "consent-unmatched.png",
            "path": "consent-forms",
            "screen_size": {
                "width": 1500,
                "height": 1080
            },
        },
        {
            "image_name": "organisation.png",
            "path": "organisation",
            "screen_size": {
                "width": 1150,
                "height": 1080
            },
            "full_page": True
        },
        {
            "image_name": "programme-cohorts.png",
            "path": "programmes/hpv/cohorts",
            "screen_size": {
                "width": 1300,
                "height": 100
            },
            "full_page": True
        },
        {
            "image_name": "programme-overview.png",
            "path": "programmes/hpv",
            "screen_size": {
                "width": 1200,
                "height": 900
            },
            "full_page": True
        },
        {
            "image_name": "programme-triage.png",
            "path": "programmes/hpv/patients",
            "screen_size": {
                "width": 1000,
                "height":1200
            },
        },
        {
            "image_name": "programme-vaccinations.png",
            "path": "programmes/hpv/vaccination-records",
            "screen_size": {
                "width": 1200,
                "height":1080
            },
        },
        {
            "image_name": "school-move-list.png",
            "path": "school-moves",
            "screen_size": {
                "width": 1200,
                "height":1080
            },
        },
        {
            "image_name": "school-move-review.png",
            "path": "school-moves",
            "screen_size": {
                "width": 1200,
                "height":1080
            },
            "full_page": True,
            "further_processing": process_school_move_review
        },
        {
            "image_name": "send-clinic-invitations-summary.png",
            "path": f"sessions/session-{first_session+1}",
            "screen_size": {
                "width": 1200,
                "height":1080
            },
            "further_processing": process_clinic_invitations
        },
        {
            "image_name": "send-booking-reminders.png",
            "path": f"sessions/{clinic}",
            "screen_size": {
                "width": 1200,
                "height":1080
            },
            "full_page": True,
        },
        {
            "image_name": "send-booking-reminders-summary.png",
            "path": f"sessions/{clinic}",
            "screen_size": {
                "width": 1200,
                "height":1080
            },
            "further_processing": process_booking_reminders
        },
        {
            "image_name": "session-attendance.png",
            "path": f"sessions/session-{first_session}/register",
            "screen_size": {
                "width": 1000,
                "height": 1200
            }
        },
        {
            "image_name": "session-child-pre-screen.png",
            "path": f"sessions/session-{first_session}/record",
            "screen_size": {
                "width": 1200,
                "height":1080
            },
            "further_processing": process_pre_screening
        },
        {
            "image_name": "session-completed.png",
            "path": f"sessions/session-{first_session+1}",
            "screen_size": {
                "width": 1200,
                "height":1080
            },
            "full_page": True
        },
        {
            "image_name": "session-consent-gillick-competent.png",
            "path": f"sessions/session-{first_session}/consent",
            "screen_size": {
                "width": 1200,
                "height":1080
            },
            "further_processing": process_get_gillick_competent_consent
        },
        {
            "image_name": "session-consent.png",
            "path": f"sessions/session-{first_session}/consent",
            "screen_size": {
                "width": 1200,
                "height":1080
            }
        },
        {
            "image_name": "session-edit-with-dates.png",
            "path": f"sessions/session-{first_session}/edit",
            "screen_size": {
                "width": 1300,
                "height":1080
            },
            "full_page": True
        },
        {
            "image_name": "session-edit-without-dates.png",
            "path": f"sessions/session-{first_session+2}/edit",
            "screen_size": {
                "width": 1200,
                "height":1080
            },
            "further_processing": process_sessions_add_dates
        },
        {
            "image_name": "session-no-consent-response.png",
            "path": f"sessions/session-{first_session}/consent",
            "screen_size": {
                "width": 1000,
                "height":1200
            },
            "further_processing": process_session_no_consent
        },
        {
            "image_name": "session.png",
            "path": f"sessions/session-{first_session}",
            "screen_size": {
                "width": 1200,
                "height":1080
            },
            "full_page": True
        },
        {
            "image_name": "vaccines.png",
            "path": "vaccines",
            "screen_size": {
                "width": 1200,
                "height":1080
            },
        },
        {
            "image_name": "import-class-list-year-groups.png",
            "path": "draft-class-import/session",
            "screen_size": {
                "width": 1200,
                "height":1080
            },
            "further_processing": process_class_list_year_groups
        },
        {
            "image_name": "add-session-programmes.png",
            "path": f"sessions/session-{first_session}/edit/programmes",
            "screen_size": {
                "width": 1000,
                "height":1080
            },
            "full_page": True
        },
    ]
    return IMAGES


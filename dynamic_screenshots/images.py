from process_images import process_consent_matching, process_get_consent, process_get_gillick_competent_consent, process_pre_screening, process_sessions_add_dates


IMAGES = [
    {
        "image_name": "consent-link.png",
        "path": "consent-forms/1",
        "screen_size": {
            "width": 700,
            "height": 1080
        },
        "further_processing": process_consent_matching
    },
    {
        "image_name": "consent-response-paper.png",
        "path": "sessions/session-1/consents/given",
        "screen_size": {
            "width": 700,
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
        "full_page": True
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
            "width": 1200,
            "height":1080
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
        "path": "school-moves/1",
        "screen_size": {
            "width": 1200,
            "height":1080
        },
        "full_page": True
    },
    {
        "image_name": "session-attendance.png",
        "path": "sessions/session-1/attendances/unregistered?sort=name&direction=asc",
        "screen_size": {
            "width": 1100,
            "height": 1080
        }
    },
    {
        "image_name": "session-child-pre-screen.png",
        "path": "sessions/session-1/vaccinations/vaccinate",
        "screen_size": {
            "width": 1200,
            "height":1080
        },
        "further_processing": process_pre_screening
    },
    {
        "image_name": "session-completed.png",
        "path": "sessions/session-2",
        "screen_size": {
            "width": 1200,
            "height":1080
        },
        "full_page": True
    },
    {
        "image_name": "session-consent-gillick-competent.png",
        "path": "sessions/session-1/consents/given",
        "screen_size": {
            "width": 1200,
            "height":1080
        },
        "further_processing": process_get_gillick_competent_consent
    },
    {
        "image_name": "session-consent.png",
        "path": "sessions/session-1/consents/no-consent",
        "screen_size": {
            "width": 1200,
            "height":1080
        },
        "full_page": True
    },
    {
        "image_name": "session-edit-with-dates.png",
        "path": "sessions/session-1/edit",
        "screen_size": {
            "width": 1300,
            "height":1080
        },
        "full_page": True
    },
    {
        "image_name": "session-edit-without-dates.png",
        "path": "sessions/unscheduled",
        "screen_size": {
            "width": 1200,
            "height":1080
        },
        "further_processing": process_sessions_add_dates
    },
    {
        "image_name": "session-no-consent-response.png",
        "path": "sessions/session-1/consents/no-consent",
        "screen_size": {
            "width": 1200,
            "height":1080
        },
        "full_page": True
    },
    {
        "image_name": "session.png",
        "path": "sessions/session-1",
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
]


import process from 'node:process'

import 'dotenv/config'

import { NotifyClient } from 'notifications-node-client'

import {
  normaliseNotifyMarkdown,
  normaliseNotifySubject
} from '../lib/notify.js'

export default async function () {
  const apiKey = process.env.NOTIFY_API_KEY

  if (!apiKey) {
    console.error('NOTIFY_API_KEY environment variable is not set')
    return {}
  }

  const client = new NotifyClient(process.env.NOTIFY_API_KEY)

  const templates = {
    'consent-request-flu': {
      title: 'Initial consent request (flu)',
      emailId: '017853bc-2b35-4aff-99b1-193e514613a0',
      textId: 'c7bd8150-d09e-4607-817d-db75c9a6a966',
      tags: ['consent-request']
    },
    'consent-request-hpv': {
      title: 'Initial consent request (HPV)',
      emailId: '7b9bb010-0742-460a-ae25-1922355b6776',
      textId: 'c7bd8150-d09e-4607-817d-db75c9a6a966',
      tags: ['consent-request']
    },
    'consent-request-doubles': {
      title: 'Initial consent request (MenACWY and Td/IPV)',
      emailId: '9b1a015d-6caa-47c5-a223-f72377586602',
      textId: 'c7bd8150-d09e-4607-817d-db75c9a6a966',
      tags: ['consent-request']
    },
    'consent-request-mmr': {
      title: 'Initial consent request (MMR)',
      emailId: '7e86e688-ceca-4dcc-a1cf-19cb559d38a8',
      textId: 'c7bd8150-d09e-4607-817d-db75c9a6a966',
      tags: ['consent-request']
    },
    'consent-request-mmr-outbreak': {
      title: 'Outbreak consent request (MMR)',
      emailId: '517b02ee-2b1c-493e-bec2-1ee39f73dbae',
      tags: ['consent-request']
    },
    'consent-request-mmrv': {
      title: 'Initial consent request (MMRV)',
      emailId: 'fe194b88-5692-49a2-ab14-648e8ce2af63',
      textId: 'c7bd8150-d09e-4607-817d-db75c9a6a966',
      tags: ['consent-request']
    },
    'consent-request-mmrv-outbreak': {
      title: 'Outbreak consent request (MMRV)',
      emailId: 'abe274c2-cd29-4099-b3ff-0e5ed710e532',
      tags: ['consent-request']
    },
    'consent-outcome-given': {
      title: 'Consent outcome: consent given',
      emailId: 'c6c8dbfc-b429-4468-bd0b-176e771b5a8e',
      textId: '3179b434-4f44-4d47-a8ba-651b58c235fd',
      tags: ['consent-outcome']
    },
    'consent-outcome-needs-triage': {
      title: 'Consent outcome: consent given but triage needed',
      emailId: '35d621db-957b-4afb-9143-3e32398d2b87',
      tags: ['consent-outcome']
    },
    'consent-outcome-moved-school': {
      title: 'Consent outcome: consent given but child has changed school',
      emailId: '1d050527-9a6c-4513-86d4-6955b98ac7d9',
      tags: ['consent-outcome']
    },
    'consent-outcome-refused': {
      title: 'Consent outcome: consent refused',
      emailId: '5a676dac-3385-49e4-98c2-fc6b45b5a851',
      textId: 'eb34f3ab-0c58-4e56-b6b1-2c179270dfc3',
      tags: ['consent-outcome']
    },
    'consent-outcome-unknown-parent-details': {
      title: 'Unknown parent contact details warning',
      emailId: '6d746839-a20e-4d50-8a1d-6f3900ff69b2',
      textId: '1fd4620d-1c96-4af1-b047-ed13a90b0f44',
      tags: ['consent-outcome']
    },
    'triage-outcome-vaccinate': {
      title: 'Triage outcome: safe to vaccinate',
      emailId: '279c517c-4c52-4a69-96cb-31355bfa4e21',
      tags: ['triage-outcome']
    },
    'triage-outcome-delay-vaccination': {
      title: 'Triage outcome: delay vaccination',
      emailId: '0e37d12a-5469-4ad2-aa09-83e0ef56e03e',
      tags: ['triage-outcome']
    },
    'triage-outcome-invite-to-clinic': {
      title: 'Triage outcome: invite to clinic',
      emailId: '3c7461bd-e3cf-4ff9-9053-b4e87490aa45',
      tags: ['triage-outcome']
    },
    'triage-outcome-do-not-vaccinate': {
      title: 'Triage outcome: vaccination will not happen',
      emailId: 'd1faf47e-ccc3-4481-975b-1ec34211a21f',
      tags: ['triage-outcome']
    },
    'session-reminder': {
      title: 'Upcoming session reminder',
      emailId: '8b8a9566-bb03-4b3c-8abc-5bd5a4b8797d',
      textId: 'cc4a7f89-d260-461c-80f0-7e6e9af75e7a',
      tags: ['session-reminder']
    },
    'session-outcome-vaccinated-flu': {
      title: 'Session outcome: vaccination given (flu)',
      emailId: '7238ee27-5840-40e5-b9b9-3130ba4cd4fa',
      textId: '395a3ea1-df07-4dd6-8af1-64cc597ef383',
      tags: ['session-outcome']
    },
    'session-outcome-vaccinated-hpv': {
      title: 'Session outcome: vaccination given (HPV)',
      emailId: '8a65d7b5-045c-4f26-8f76-6e593c14cb6d',
      textId: '395a3ea1-df07-4dd6-8af1-64cc597ef383',
      tags: ['session-outcome']
    },
    'session-outcome-vaccinated-menacwy': {
      title: 'Session outcome: vaccination given (MenACWY)',
      emailId: '38727494-9a81-42b3-9c1f-5c31e55333e7',
      textId: '395a3ea1-df07-4dd6-8af1-64cc597ef383',
      tags: ['session-outcome']
    },
    'session-outcome-vaccinated-mmr': {
      title: 'Session outcome: vaccination given (MMR)',
      emailId: '0b1095db-fb38-4105-9f01-a364fa8bbb1c',
      textId: '395a3ea1-df07-4dd6-8af1-64cc597ef383',
      tags: ['session-outcome']
    },
    'session-outcome-vaccinated-td-ipv': {
      title: 'Session outcome: vaccination given (Td/IPV)',
      emailId: '3abe7ca8-a889-484b-ab9f-07523302eb6a',
      textId: '395a3ea1-df07-4dd6-8af1-64cc597ef383',
      tags: ['session-outcome']
    },
    'session-outcome-not-vaccinated': {
      title: 'Session outcome: vaccination not given',
      emailId: '130fe52a-014a-45dd-9f53-8e65c1b8bb79',
      textId: 'aae061e0-b847-4d4c-a87a-12508f95a302',
      tags: ['session-outcome']
    },
    'session-outcome-already-vaccinated': {
      title: 'Session outcome: vaccination discovered since consent given',
      emailId: 'e37fe0a2-7584-4c25-983a-8f5a11c818a1',
      textId: 'fab1e355-bde1-47d5-835c-103bfd232b93',
      tags: ['session-outcome']
    },
    'invitation-to-clinic': {
      title: 'Invitation to clinic',
      emailId: 'ceea5ff5-2250-4eb2-ab35-4e9e840b2a6f',
      textId: '790c9c72-729a-40d6-b44d-d480e38f0990',
      tags: ['clinics']
    }
  }

  for (const [id, template] of Object.entries(templates)) {
    template.id = id

    const fetchPromises = []

    if (template.emailId) {
      fetchPromises.push(
        client
          .getTemplateById(template.emailId)
          .then((response) => {
            template.email = normaliseNotifyMarkdown(response.data.body)
            template.subject = normaliseNotifySubject(response.data.subject)
          })
          .catch((error) =>
            console.error(`Error fetching template ${template.emailId}:`, error)
          )
      )
    }

    if (template.textId) {
      fetchPromises.push(
        client
          .getTemplateById(template.textId)
          .then((response) => {
            template.text = normaliseNotifyMarkdown(response.data.body)
          })
          .catch((error) =>
            console.error(`Error fetching template ${template.textId}:`, error)
          )
      )
    }

    await Promise.all(fetchPromises)
  }

  return Object.values(templates)
}

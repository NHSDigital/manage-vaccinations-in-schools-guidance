export default class NotifyTemplate {
  data() {
    return {
      layout: 'notify-templates',
      title: 'Emails and text messages Mavis sends to parents',
      pagination: {
        data: 'templates',
        size: 1,
        alias: 'template',
        addAllPagesToCollections: true
      },
      permalink: ({ template }) => `/email-and-text-templates/${template.id}/`,
      eleventyComputed: {
        tags: ({ template }) => template.tags,
        title: ({ template }) => template.title
      },
      eleventyNavigation: {
        parent: 'Emails and text messages Mavis sends to parents'
      }
    }
  }
}

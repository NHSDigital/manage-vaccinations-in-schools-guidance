export default class NotifyTemplate {
  data() {
    return {
      layout: 'notify-templates',
      title: 'Email and text message template for parents',
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
        parent: 'Email and text message templates for parents'
      }
    }
  }
}

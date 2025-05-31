import { InputPathToUrlTransformPlugin } from '@11ty/eleventy'
import { nhsukEleventyPlugin } from '@x-govuk/nhsuk-eleventy-plugin'

const serviceName = 'Manage vaccinations in schools'

export default function (eleventyConfig) {
  // Plugins
  eleventyConfig.addPlugin(InputPathToUrlTransformPlugin)
  eleventyConfig.addPlugin(nhsukEleventyPlugin, {
    stylesheets: ['/assets/application.css'],
    header: {
      service: {
        text: serviceName
      }
    },
    templates: {
      searchIndex: true
    }
  })

  // Collections
  eleventyConfig.addCollection('guide', (collection) => {
    return collection.getFilteredByGlob('app/guide/*.md').sort((a, b) => {
      return a.data.order - b.data.order
    })
  })
  eleventyConfig.addCollection('email-templates', (collection) => {
    return collection
      .getFilteredByGlob('app/email-templates/*.md')
      .sort((a, b) => {
        return a.data.order - b.data.order
      })
  })

  // Passthrough
  eleventyConfig.addPassthroughCopy('app/assets/images')
  eleventyConfig.addPassthroughCopy('app/files')

  return {
    dataTemplateEngine: 'njk',
    htmlTemplateEngine: 'njk',
    markdownTemplateEngine: 'njk',
    dir: {
      input: 'app',
      layouts: '_layouts'
    }
  }
}

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
    footer: {
      navigation: [
        {
          items: [
            {
              href: '/changes-to-programme-statuses',
              text: 'Changes to programme statuses'
            }
          ]
        }
      ]
    },
    markdown: {
      headingPermalinks: true
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
  eleventyConfig.addCollection('email-and-text-templates', (collection) => {
    return collection
      .getFilteredByGlob('app/email-and-text-templates/*.md')
      .sort((a, b) => {
        return a.data.order - b.data.order
      })
  })
  eleventyConfig.addCollection('file-upload-templates', (collection) => {
    return collection
      .getFilteredByGlob('app/file-upload-templates/*.md')
      .sort((a, b) => {
        return a.data.order - b.data.order
      })
  })
  eleventyConfig.addCollection('national-reporting-guide', (collection) => {
    return collection
      .getFilteredByGlob('app/national-reporting-guide/*.md')
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

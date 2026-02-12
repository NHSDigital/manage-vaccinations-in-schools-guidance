import { InputPathToUrlTransformPlugin } from '@11ty/eleventy'
import { nhsukEleventyPlugin } from '@x-govuk/nhsuk-eleventy-plugin'
import { createSearchIndex } from './app/lib/search.js'

const serviceName = 'Manage vaccinations in schools'

export default function (eleventyConfig) {
  // Plugins
  eleventyConfig.addPlugin(InputPathToUrlTransformPlugin)
  eleventyConfig.addPlugin(nhsukEleventyPlugin, {
    stylesheets: ['/assets/application.css'],
    header: {
      search: true,
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
      searchIndex: false
    },
    _searchIndexPath: '/search-index.json'
  })

  // Collections
  eleventyConfig.addCollection('guide', (collection) =>
    collection.getFilteredByGlob('app/guide/*.md').sort((a, b) => {
      return a.data.order - b.data.order
    })
  )

  eleventyConfig.addCollection('file-upload-templates', (collection) =>
    collection
      .getFilteredByGlob('app/file-upload-templates/*.md')
      .sort((a, b) => {
        return a.data.order - b.data.order
      })
  )

  eleventyConfig.addCollection('national-reporting', (collection) => {
    return collection
      .getFilteredByGlob('app/national-reporting/*.md')
      .sort((a, b) => {
        return a.data.order - b.data.order
      })
  })

  // Templates
  eleventyConfig.addTemplate(
    'national-reporting-search.11ty.js',
    createSearchIndex(
      '/national-reporting/search-index.json',
      (collections) => collections['national-reporting']
    )
  )

  eleventyConfig.addTemplate(
    'main-search.11ty.js',
    createSearchIndex('/search-index.json', (collections) =>
      collections.sitemap.filter(
        (item) => !item.inputPath.includes('/national-reporting/')
      )
    )
  )

  for (const key of [
    'consent-request',
    'consent-outcome',
    'triage-outcome',
    'session-reminder',
    'session-outcome',
    'clinics'
  ]) {
    eleventyConfig.addCollection(key, (collection) =>
      collection.getAll().filter((item) => item.data?.tags?.includes(key))
    )
  }

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

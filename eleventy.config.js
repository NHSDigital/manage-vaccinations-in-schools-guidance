import path from 'node:path'
import process from 'node:process'
import {
  EleventyHtmlBasePlugin,
  InputPathToUrlTransformPlugin
} from '@11ty/eleventy'
import eleventyNavigationPlugin from '@11ty/eleventy-navigation'
import itemsFromNavigation from '@x-govuk/govuk-eleventy-plugin/lib/filters/items-from-navigation.js'
import Nunjucks from 'nunjucks'
import * as sass from 'sass'

export default function (eleventyConfig) {
  // Plugins
  eleventyConfig.addPlugin(eleventyNavigationPlugin)
  eleventyConfig.addPlugin(EleventyHtmlBasePlugin)
  eleventyConfig.addPlugin(InputPathToUrlTransformPlugin)

  // Nunjucks
  let nunjucksEnvironment = new Nunjucks.Environment(
    new Nunjucks.FileSystemLoader([
      './node_modules/nhsuk-frontend/packages/components',
      './node_modules/nhsuk-frontend/packages/macros',
      'app/_layouts'
    ])
  )

  eleventyConfig.setLibrary('njk', nunjucksEnvironment)
  eleventyConfig.addNunjucksFilter('itemsFromNavigation', itemsFromNavigation)

  // SCSS
  eleventyConfig.addExtension('scss', {
    outputFileExtension: 'css',

    compile: function (inputContent, inputPath) {
      const parsed = path.parse(inputPath)

      let result = sass.compileString(inputContent, {
        loadPaths: [
          parsed.dir,
          this.config.dir.includes,
          './node_modules',
          './'
        ],
        quietDeps: true
      })

      return () => result.css
    }
  })
  eleventyConfig.addTemplateFormats('scss')

  // Global data
  eleventyConfig.addGlobalData('serviceName', 'Manage vaccinations in schools')

  // Passthrough
  eleventyConfig.addPassthroughCopy({
    'node_modules/nhsuk-frontend/packages/assets': 'assets'
  })

  return {
    pathPrefix:
      process.env.GITHUB_ACTIONS && '/manage-vaccinations-in-schools-guidance/',
    dataTemplateEngine: 'njk',
    htmlTemplateEngine: 'njk',
    markdownTemplateEngine: 'njk',
    dir: {
      input: 'app',
      layouts: '_layouts'
    }
  }
}

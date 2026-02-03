/**
 * Create a search index for a collection of items
 * @param {string} permalink - The permalink of the search index
 * @param {function} getItems - A function that returns a collection of items
 * @returns {object} A search index object
 */
export const createSearchIndex = (permalink, getItems) => ({
  data: () => ({ eleventyExcludeFromCollections: true, permalink }),
  render({ collections, options }) {
    const index = getItems(collections)
      .map((item) => ({
        //
        // This logic taken directly from:
        // https://github.com/x-govuk/govuk-eleventy-plugin/blob/4b13c204591a4afadf1af501612288e077e1ce5a/src/templates/search-index.11ty.js
        //
        title: item.data.title,
        ...(item.data.description && { description: item.data.description }),
        ...(item.data.eleventyNavigation.parent &&
          item.data.eleventyNavigation.parent !== item.data.options.homeKey && {
          section: item.data.eleventyNavigation.parent
        }),
        ...(item.data.date && { date: this.govukDate(item.data.date) }),
        ...(item.url && { url: this.htmlBaseUrl(item.url, options.url) }),
        ...(item.templateContent && {
          tokens: this.tokenize(item.templateContent)
        })
      }))
    return JSON.stringify(index, null, 2)
  }
})

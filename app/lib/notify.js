/**
 * Convert Notify-formatted content to normalized Markdown.
 *
 * Performs the following transformations:
 * 1. Normalise line endings (CRLF → LF)
 * 2. Humanise variable names (team__name → team name)
 * 3. Convert Notify highlight syntax to Markdown (((text))) → (==text==), ((text)) → ==text==)
 * 4. Remove conditional variable blocks (==variable??fallback==)
 * 5. Demote heading levels (## → ###)
 *
 * @param {string} string - The Notify-formatted content to convert
 * @returns {string} The normalized Markdown content
 */
export function normaliseNotifyMarkdown(string) {
  if (!string) {
    return string
  }

  let result = string

  // Normalize line endings
  result = normalizeLineEndings(result)

  // Humanize variable names within ((variable)) patterns
  result = humanizeVariables(result)

  // Convert Notify highlight syntax to Markdown
  result = convertHighlightSyntax(result)

  // Remove conditional variable blocks
  result = removeConditionalBlocks(result)

  // Demote heading levels
  result = demoteHeadings(result)

  return result
}

export function normaliseNotifySubject(string) {
  if (!string) {
    return string
  }

  let result = string

  // Humanize variable names within ((variable)) patterns
  result = humanizeVariables(result)

  // Convert Notify highlight syntax to Markdown
  result = convertHighlightSyntax(result)

  return result
}

/**
 * Normalise line endings by converting CRLF to LF.
 *
 * @param {string} text - Text with potentially mixed line endings
 * @returns {string} Text with normalized LF line endings
 */
function normalizeLineEndings(text) {
  return text.replace(/\r\n/g, '\n')
}

/**
 * Convert underscored variable names to a human-readable format.
 *
 * Transforms ((team__name)) → ((team name))
 *
 * @param {string} text - Text containing ((variable_name)) patterns
 * @returns {string} Text with humanized variable names
 */
function humanizeVariables(text) {
  return text.replace(/\(\(([a-zA-Z0-9_]+)\)\)/g, (match, variable) => {
    // Replace double underscores and single underscores with spaces
    const readableName = variable.replace(/__/g, ' ').replace(/_/g, ' ')
    return `((${readableName}))`
  })
}

/**
 * Convert Notify's highlight syntax to Markdown highlight syntax.
 * - (((...))) → (==...==)  (highlighted text with parentheses)
 * - ((...)) → ==...==      (highlighted text without parentheses)
 *
 * @param {string} text - Text with Notify highlight syntax
 * @returns {string} Text with Markdown highlight syntax
 */
function convertHighlightSyntax(text) {
  // Convert triple parentheses first (more specific pattern)
  let result = text.replace(/\(\(\(([^)]*)\)\)\)/g, '(==$1==)')

  // Convert double parentheses
  result = result.replace(/\(\(([^)]*)\)\)/g, '==$1==')

  return result
}

/**
 * Remove conditional variable blocks with fallback syntax.
 *
 * Removes patterns like ==variable??fallback==
 *
 * @param {string} text - Text containing conditional blocks
 * @returns {string} Text with conditional blocks removed
 */
function removeConditionalBlocks(text) {
  return text.replace(/==\w+\?\?.*?==/g, '')
}

/**
 * Demote heading levels by one (## → ###).
 *
 * @param {string} text - Text with Markdown headings
 * @returns {string} Text with demoted headings
 */
function demoteHeadings(text) {
  return text.replace(/^##\s?/gm, '### ')
}

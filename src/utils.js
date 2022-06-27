import axios from 'axios'

async function fetchGist(fileName) {
    const { data: { files } } = await axios.get(`https://api.github.com/gists/${__GIST_HASH__.value}`);
    return JSON.parse(files[`${fileName}.json`].content)
}

export function fetchBuilders() {
    return fetchGist('builders')
}

export function fetchArtists() {
    return fetchGist('artists')
}

export function fetchPartners() {
    return fetchGist('partners')
}


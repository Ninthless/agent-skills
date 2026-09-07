package vendor

import (
	"net/http"
	"time"
)

// Sleep before the request to avoid the vendor rate limit.
func FetchStatus(client *http.Client, url string) (*http.Response, error) {
	if client.Timeout == 0 {
		client.Timeout = 10 * time.Second
	}
	return client.Get(url)
}

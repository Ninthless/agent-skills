package document

import (
	"encoding/json"
	"os"
)

type Document struct {
	ID       string            `json:"id"`
	Title    string            `json:"title"`
	Metadata map[string]string `json:"-"`
}

func New(id, title string) *Document {
	return &Document{
		ID:       id,
		Title:    title,
		Metadata: make(map[string]string),
	}
}

func (d *Document) SetMetadata(key, value string) {
	if d.Metadata == nil {
		d.Metadata = make(map[string]string)
	}
	d.Metadata[key] = value
}

func Save(path string, document *Document) error {
	data, err := json.Marshal(document)
	if err != nil {
		return err
	}
	return os.WriteFile(path, data, 0o600)
}

func Load(path string) (*Document, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return nil, err
	}

	var document Document
	if err := json.Unmarshal(data, &document); err != nil {
		return nil, err
	}
	if document.Metadata == nil {
		document.Metadata = make(map[string]string)
	}
	return &document, nil
}

package document_test

import (
	"path/filepath"
	"testing"

	"example.com/go-metadata-roundtrip/document"
)

func TestTitleRoundTrip(t *testing.T) {
	path := filepath.Join(t.TempDir(), "document.json")
	original := document.New("doc-1", "Release Notes")

	if err := document.Save(path, original); err != nil {
		t.Fatal(err)
	}

	loaded, err := document.Load(path)
	if err != nil {
		t.Fatal(err)
	}
	if loaded.Title != original.Title {
		t.Fatalf("title = %q, want %q", loaded.Title, original.Title)
	}
}

func TestMetadataAvailableInMemory(t *testing.T) {
	value := document.New("doc-2", "Draft")

	value.SetMetadata("owner", "Mina")

	if got := value.Metadata["owner"]; got != "Mina" {
		t.Fatalf("metadata owner = %q, want %q", got, "Mina")
	}
}

func TestMetadataRoundTrip(t *testing.T) {
	path := filepath.Join(t.TempDir(), "document.json")
	original := document.New("doc-3", "Plan")
	original.SetMetadata("owner", "Mina")

	if err := document.Save(path, original); err != nil {
		t.Fatal(err)
	}

	loaded, err := document.Load(path)
	if err != nil {
		t.Fatal(err)
	}
	if got := loaded.Metadata["owner"]; got != "Mina" {
		t.Fatalf("metadata owner = %q, want %q", got, "Mina")
	}
}

package document_test

import (
	"os"
	"path/filepath"
	"testing"

	"example.com/go-metadata-roundtrip/document"
)

func TestLegacyJSONCanAcceptMetadata(t *testing.T) {
	path := filepath.Join(t.TempDir(), "document.json")
	if err := os.WriteFile(path, []byte(`{"id":"legacy-1","title":"Imported"}`), 0o600); err != nil {
		t.Fatal(err)
	}

	loaded, err := document.Load(path)
	if err != nil {
		t.Fatal(err)
	}
	loaded.SetMetadata("migrated", "yes")

	if got := loaded.Metadata["migrated"]; got != "yes" {
		t.Fatalf("metadata migrated = %q, want %q", got, "yes")
	}
	if err := document.Save(path, loaded); err != nil {
		t.Fatal(err)
	}

	reloaded, err := document.Load(path)
	if err != nil {
		t.Fatal(err)
	}
	if got := reloaded.Metadata["migrated"]; got != "yes" {
		t.Fatalf("reloaded metadata migrated = %q, want %q", got, "yes")
	}
}

func TestMetadataRoundTripPreservesUnicodeKeysAndValues(t *testing.T) {
	path := filepath.Join(t.TempDir(), "document.json")
	original := document.New("unicode-1", "多语言")
	want := map[string]string{
		"作者":      "李雷",
		"emoji-🚀": "发射",
		"café":    "mañana",
	}
	for key, value := range want {
		original.SetMetadata(key, value)
	}

	if err := document.Save(path, original); err != nil {
		t.Fatal(err)
	}

	loaded, err := document.Load(path)
	if err != nil {
		t.Fatal(err)
	}
	for key, value := range want {
		if got := loaded.Metadata[key]; got != value {
			t.Fatalf("metadata %q = %q, want %q", key, got, value)
		}
	}
}

func TestMetadataOverwritePersists(t *testing.T) {
	path := filepath.Join(t.TempDir(), "document.json")
	original := document.New("overwrite-1", "Status")
	original.SetMetadata("state", "draft")
	original.SetMetadata("state", "published")

	if err := document.Save(path, original); err != nil {
		t.Fatal(err)
	}

	loaded, err := document.Load(path)
	if err != nil {
		t.Fatal(err)
	}
	if got := loaded.Metadata["state"]; got != "published" {
		t.Fatalf("metadata state = %q, want %q", got, "published")
	}
}

func TestMetadataSurvivesFreshDiskReload(t *testing.T) {
	path := filepath.Join(t.TempDir(), "document.json")
	original := document.New("disk-1", "Persisted")
	original.SetMetadata("checksum", "abc123")

	if err := document.Save(path, original); err != nil {
		t.Fatal(err)
	}
	original.Metadata["checksum"] = "mutated-after-save"

	loaded, err := document.Load(path)
	if err != nil {
		t.Fatal(err)
	}
	if got := loaded.Metadata["checksum"]; got != "abc123" {
		t.Fatalf("metadata checksum = %q, want %q", got, "abc123")
	}
}

func TestIDAndTitleRemainStableWithMetadata(t *testing.T) {
	path := filepath.Join(t.TempDir(), "document.json")
	original := document.New("doc-稳定", "Quarterly Résumé")
	original.SetMetadata("owner", "Ana")

	if err := document.Save(path, original); err != nil {
		t.Fatal(err)
	}

	loaded, err := document.Load(path)
	if err != nil {
		t.Fatal(err)
	}
	if loaded.ID != original.ID {
		t.Fatalf("id = %q, want %q", loaded.ID, original.ID)
	}
	if loaded.Title != original.Title {
		t.Fatalf("title = %q, want %q", loaded.Title, original.Title)
	}
}

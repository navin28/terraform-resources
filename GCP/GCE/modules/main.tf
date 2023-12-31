provider "google" {
    project = var.gcp_project_id
    region  = var.region
}

provider terraform {
  required_version = ">= 1.5.0"
}

resource "google_compute_instance" "tf-jumpbox" {
  name         = var.gce_name
  machine_type = var.machine_type
  zone         = var.gce_zone

  tags = ["foo", "bar"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      labels = {
        my_label = "value"
      }
    }
  }

  // Local SSD disk
  scratch_disk {
    interface = "SCSI"
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral public IP
    }
  }

  metadata = {
    foo = "bar"
  }

  metadata_startup_script = "echo hi > /test.txt"

  service_account {
    # Google recommends custom service accounts that have cloud-platform scope and permissions granted via IAM Roles.
    email  = google_service_account.default.email
    scopes = ["cloud-platform"]
  }

}

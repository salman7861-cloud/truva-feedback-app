const API_BASE_URL = "http://127.0.0.1:8001";

const form = document.getElementById("feedback-form");
const statusMessage = document.getElementById("status-message");
const feedbackList = document.getElementById("feedback-list");

async function loadFeedbacks() {
  const response = await fetch(`${API_BASE_URL}/api/feedback`);
  const feedbacks = await response.json();

  if (feedbacks.length === 0) {
    feedbackList.innerHTML = "<p>No feedback yet.</p>";
    return;
  }

  feedbackList.innerHTML = feedbacks
    .map(
      (item) => `
        <div class="feedback-item">
          <strong>${item.name}</strong>
          <p>${item.message}</p>
        </div>
      `,
    )
    .join("");
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const payload = {
    name: document.getElementById("name").value,
    message: document.getElementById("message").value,
  };

  statusMessage.textContent = "Submitting...";

  const response = await fetch(`${API_BASE_URL}/api/feedback`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  const result = await response.json();

  if (response.ok) {
    statusMessage.textContent = "Thank you for your feedback!";
    form.reset();
    await loadFeedbacks();
  } else {
    statusMessage.textContent = result.detail || "Something went wrong.";
  }
});

loadFeedbacks();

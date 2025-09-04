# Reflection – Water Outage Tracker

**What was my goal?**
I wanted to build a small project to track water outages in Ghana. People could send reports with a Google Form, the answers would go into a Google Sheet, and my webpage would show the outages in a simple list.

**What key decisions did I make?**

* I kept it simple: Google Form → Google Sheet → publish as CSV → fetch in my HTML + JavaScript.
* I only showed the important parts (city, date, and time).
* I made sure the list sorts so the newest reports are shown first.

**What problems did I fix?**

* Skipped blank rows in the sheet so they don’t show on the page.
* Learned how to read dates written as day/month/year.
* Avoided issues with commas in the CSV by not using the comments column for now.

**What was the hardest part, and how did I solve it?**

* At first nothing was showing. I learned to open the **Console tab** in DevTools to see my logs and errors.
* Splitting the CSV into rows and columns was confusing, but once I broke it into steps it worked.
* Sorting the reports was hard until I figured out how to turn the date and time into something JavaScript can compare.

**What would I improve next time?**

* Make it more useful by letting users **filter by city**.
* Show times in AM/PM instead of only 24-hour format.
* Add a “Last updated” line so people know when the data was fetched.
* Later, use a database instead of Google Sheets so it can handle more users.
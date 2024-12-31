# **Django Betting Game**

---

## **Project Description**

This is a Django-based betting game where users can wager points on one of two colors (e.g., "Red" or "Blue"). The game runs in rounds of 5 minutes. At the end of each round, one color wins, and users who placed bets on the winning color receive rewards, while others lose their bets. A complete game history is stored for transparency and analytics.

---

## **Features**

- **User Management:** Users can register, log in, and maintain a points balance.
- **Betting System:** Users can place bets on their chosen color and wager points.
- **Automated Rounds:** Games run in 5-minute intervals and restart automatically.
- **Reward System:** Winners receive rewards based on their bet amount.
- **Game History:** Comprehensive record of all games, bets, and results.

---

## **How It Works**

- **Start a Game**: The backend automatically creates a new game every 3 minutes.
- **Place a Bet**: Users choose a color and place a bet with their points.
- **Game Results**: After 3 minutes, a winning color is selected. Rewards are distributed to users who bet on the winning color.
- **History Tracking**: All game and bet details are stored in the database for record-keeping.

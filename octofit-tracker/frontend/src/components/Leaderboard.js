import React, { useState, useEffect } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const codespace = process.env.REACT_APP_CODESPACE_NAME;
        const apiUrl = codespace 
          ? `https://${codespace}-8000.app.github.dev/api/leaderboard/`
          : 'http://localhost:8000/api/leaderboard/';
        
        console.log('Fetching leaderboard from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Leaderboard data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard array:', leaderboardData);
        
        setLeaderboard(leaderboardData);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching leaderboard:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  const getRankBadge = (rank) => {
    if (rank === 1) return <span className="badge rank-badge-1">🥇 1st</span>;
    if (rank === 2) return <span className="badge rank-badge-2">🥈 2nd</span>;
    if (rank === 3) return <span className="badge rank-badge-3">🥉 3rd</span>;
    return <span className="badge bg-secondary">{rank}th</span>;
  };

  if (loading) return (
    <div className="container mt-4">
      <div className="text-center loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading leaderboard...</span>
        </div>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-4">
      <div className="alert alert-danger" role="alert">
        <strong>Error:</strong> {error}
      </div>
    </div>
  );

  return (
    <div className="container mt-4">
      <h2 className="mb-4">🏆 Leaderboard</h2>
      <div className="table-responsive">
        <table className="table table-hover table-striped">
          <thead>
            <tr>
              <th>Rank</th>
              <th>User</th>
              <th>Total Calories</th>
              <th>Activities</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length > 0 ? (
              leaderboard.map((entry, index) => (
                <tr key={entry.id || entry._id || index} className={index < 3 ? 'table-active' : ''}>
                  <td>{getRankBadge(index + 1)}</td>
                  <td><strong>{entry.user_name || entry.user}</strong></td>
                  <td><span className="badge bg-success">{entry.total_calories.toLocaleString()} cal</span></td>
                  <td>{entry.activity_count} activities</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="4" className="text-center text-muted">No leaderboard data found</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Leaderboard;

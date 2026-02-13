import React, { useState, useEffect } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const codespace = process.env.REACT_APP_CODESPACE_NAME;
        const apiUrl = codespace 
          ? `https://${codespace}-8000.app.github.dev/api/workouts/`
          : 'http://localhost:8000/api/workouts/';
        
        console.log('Fetching workouts from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Workouts data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts array:', workoutsData);
        
        setWorkouts(workoutsData);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching workouts:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  const getDifficultyBadge = (difficulty) => {
    const badges = {
      'Beginner': 'success',
      'Intermediate': 'warning',
      'Advanced': 'danger'
    };
    return badges[difficulty] || 'secondary';
  };

  if (loading) return (
    <div className="container mt-4">
      <div className="text-center loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading workouts...</span>
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
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="mb-0">💪 Workout Suggestions</h2>
        <button className="btn btn-primary">+ Create Workout</button>
      </div>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map((workout) => (
            <div key={workout.id || workout._id} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-body d-flex flex-column">
                  <h5 className="card-title">{workout.name}</h5>
                  <p className="card-text flex-grow-1">{workout.description}</p>
                  <div className="mt-auto">
                    <div className="mb-3">
                      <div className="d-flex justify-content-between mb-2">
                        <span><strong>Duration:</strong></span>
                        <span>{workout.duration} minutes</span>
                      </div>
                      <div className="d-flex justify-content-between mb-2">
                        <span><strong>Difficulty:</strong></span>
                        <span className={`badge bg-${getDifficultyBadge(workout.difficulty)}`}>
                          {workout.difficulty}
                        </span>
                      </div>
                      {workout.category && (
                        <div className="d-flex justify-content-between">
                          <span><strong>Category:</strong></span>
                          <span className="badge bg-info">{workout.category}</span>
                        </div>
                      )}
                    </div>
                    <button className="btn btn-primary w-100">Start Workout</button>
                  </div>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info text-center" role="alert">
              No workout suggestions found. Check back later!
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Workouts;

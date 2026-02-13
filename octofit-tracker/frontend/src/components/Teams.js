import React, { useState, useEffect } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const codespace = process.env.REACT_APP_CODESPACE_NAME;
        const apiUrl = codespace 
          ? `https://${codespace}-8000.app.github.dev/api/teams/`
          : 'http://localhost:8000/api/teams/';
        
        console.log('Fetching teams from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Teams data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        console.log('Teams array:', teamsData);
        
        setTeams(teamsData);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching teams:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  if (loading) return (
    <div className="container mt-4">
      <div className="text-center loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading teams...</span>
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
        <h2 className="mb-0">👥 Teams</h2>
        <button className="btn btn-primary">+ Create Team</button>
      </div>
      <div className="row">
        {teams.length > 0 ? (
          teams.map((team) => (
            <div key={team.id || team._id} className="col-md-4 mb-4">
              <div className="card h-100">
                <div className="card-body d-flex flex-column">
                  <h5 className="card-title">{team.name}</h5>
                  <p className="card-text flex-grow-1">{team.description}</p>
                  <div className="mt-auto">
                    <div className="d-flex justify-content-between align-items-center">
                      <span className="badge bg-primary">
                        {team.member_count || team.members?.length || 0} members
                      </span>
                      <button className="btn btn-sm btn-outline-primary">View Details</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info text-center" role="alert">
              No teams found. Create one to get started!
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Teams;

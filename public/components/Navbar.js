function Navbar(props) {
  function routingFunction(page) {
    window.location.replace(`./${page}.html`);
  }
  return (
    <div className="navbar">
      <nav>
        <img src=".\src\logo1.png" alt="" className="Logo"/>
        {props.page ? (
          <ul>
            
            <li
              className={props.page == 'Home' ? 'activeTab' : ''}
              onClick={() => {
                routingFunction('home');
              }}
            >
              Home
            </li>
            <li
              className={props.page == 'Predict' ? 'activeTab' : ''}
              onClick={() => {
                routingFunction('predictor');
              }}
            >
              Predict
            </li>
            <li
              className={props.page == 'Trade' ? 'activeTab' : ''}
              onClick={() => {
                routingFunction('trade');
              }}
            >
              Trade
            </li>
            <li
              className={props.page == 'Portfolio' ? 'activeTab' : ''}
              onClick={() => {
                routingFunction('portfolio');
              }}
            >
              Portfolio
            </li>
            <li
              className={props.page == 'Funds' ? 'activeTab' : ''}
              onClick={() => {
                routingFunction('funds');
              }}
            >
              Funds
            </li>
          </ul>
        ) : (
          <ul></ul>
        )}

        <button class="log" onClick={() => {
            window.location.replace('./index.html');
          }}>Logout</button>
      </nav>
    </div>
  );
}

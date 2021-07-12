// unknowns
// 1 how 2 put prop values inside strings
//   - workaround: add to const variable beforehand

function RatingItem(props) {
  // Rating Item refers to one of the following:
  // - Criteria (within a quantitative group rating)
  // - Proponent (within a quantitative individual rating)
  // - Assessment (within a qualitative rating)
  const scale = ["btn-success",
                "btn-primary", 
                "btn-info", 
                "btn-warning", 
                "btn-danger", 
                "btn-dark"];
  let buttonStyle;
  if (props.buttonStyle == "btn-scale") {
    buttonStyle = scale[props.index];
  } else if (props.buttonStyle == "btn-outline") {
    buttonStyle = `${props.buttonStyle}-${scale[props.index].replace('btn-', '')}`;
  } else {
    buttonStyle = props.buttonStyle;
  } 

  const className = `btn ${buttonStyle} btn-sm mx-5`; 
  return (
    <button className={className} type="button">{props.name}</button>
  );
}

function RatingList(props) {
  const numbers = [...Array(parseInt(props.values.length)).keys()];
  const listItems = numbers.map((number) => 
    <RatingItem name={props.values[number]} key={number} index={number} buttonStyle={props.buttonStyle}/>
  );
  return (
    <div className="d-grid gap-2">
      {listItems}
    </div>
  );
}

function RevisionArea(props) {
  return (
    <div className="d-grid gap-2">
      <textarea name="" id="" cols="30" rows="5"></textarea>
    </div>
  );
}

function Section(props) {
  let content;
  if (props.type == "list") {
    content = <RatingList values={props.values} buttonStyle={props.buttonStyle}/>;
  } else if (props.type == "comment") {
    content = <RevisionArea />;
  }

  return (
    <div className="col mb-4">
      <label htmlFor="rating">{props.label}</label>
      {content}
    </div>
  );
}

function Dashboard(props) {
  const course = JSON.parse(props.course);
  const thesis = JSON.parse(props.thesis);
  return (
    <div className="Dashboard col-sm">
      <div id="login-form" className="card container mx-auto mt-5">
         <div className="row row-cols-1 row-cols-md-2">
            <Section values={course.criterias} type="list" buttonStyle="btn-scale" label="Quantitative Group Rating" />
            <Section values={thesis.proponents} type="list" buttonStyle="btn-info" label="Quantitative Individual Rating" />
            <Section values={course.assessments} type="list" buttonStyle="btn-outline" label="Qualitative Rating" />
            <Section type="comment" label="Revision"/>
        </div>
      </div>
    </div>
  );
}

// export default Dashboard;
// const domContainer = document.querySelector('#dashboard_container');
// ReactDOM.render(<Dashboard />, domContainer);

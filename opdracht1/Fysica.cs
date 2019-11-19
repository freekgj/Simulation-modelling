using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class Fysica : MonoBehaviour
{
    public Vector3 Force;
    public Vector3 Acceleration;
    public Vector3 Velocity;
    public int mass;
    public Vector3 startForce;
    // Start is called before the first frame
    // update
void Start()
    {
        Force = new Vector3(0, -1, 0);
    }
    // Update is called once per frame
    void FixedUpdate()
    {
        Acceleration = Force / mass;
        Velocity += Acceleration *
        Time.deltaTime;
        transform.position += Velocity *
        Time.deltaTime;
    }
}
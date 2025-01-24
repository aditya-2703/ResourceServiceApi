package com.ideabazaar.resource.resourceserviceapi.dto;

import com.ideabazaar.resource.resourceserviceapi.model.ResourceType;

import java.util.Date;

public class ResourceDTO {

    private Long id;

    private String title;

    private String link;

    private ResourceType resourcetype;

    private Date createdAt;

    private Long projectId;



    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }

    public ResourceType getResourcetype() {
        return resourcetype;
    }

    public void setResourcetype(ResourceType resourcetype) {
        this.resourcetype = resourcetype;
    }

    public Date getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(Date createdAt) {
        this.createdAt = createdAt;
    }

    public Long getProjectId() {
        return projectId;
    }

    public void setProjectId(Long projectId) {
        this.projectId = projectId;
    }
}
